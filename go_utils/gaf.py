import re, sys
import pandas as pd
import numpy as np
class gaf:
    """A simple class for reading or generating gaf files"""
    annotations = pd.DataFrame()
    def read_gaf(self,infile):
        obofile = open(infile,"r")
        lines = obofile.readlines()
        if self.check_gaf_version(lines):
            self.annotations = self.get_annotations_from_gaf(lines)
            self.annotations = self.annotations.reindex_axis(self.gaf_2_x_fields,1)
        else:
             sys.exit("The input is not a gaf file.\nPlease check the input file for errors")

    def check_gaf_version(self,lines):
        comment_lines =  [s for s in lines[1:20] if "!" in s]
        gaf_line = map(re.compile(r'!gaf-version\s*:\s*2\..').search,comment_lines)
        if len(gaf_line)>0:
            return True
        else:
            return False

    def get_annotations_from_gaf(self,lines):
        tmp_annotations = []
        col_ids = self.gaf_2_x_fields
        for index,line in enumerate(lines):
            if "!" in line:
                continue
            else:
                line = line.strip("\n")
                col_data = line.split("\t")
                col_dict = dict(zip(col_ids,col_data))
                tmp_annotations.append(col_dict)
            if index % 100 == 0:
                print "Processed %s lines" % (index)
        gaf_df = pd.DataFrame.from_dict(tmp_annotations,"columns")
        return gaf_df


    def write_gaf(self,outfile="test.out",col_name="with",th=0):
        if self.annotations.shape[1] < 17:
            sys.stderr.write("Number of columns do not match gaf 2.0 format\n")
            all_cols = set(self.gaf_2_x_fields)
            exist_cols = set(self.annotations.columns)
            need_cols = all_cols.difference(exist_cols)
            ", ".join(need_cols)
            sys.stderr.write("%s\n" % ", ".join(need_cols))
            return None

        gaf_out = open(outfile,"w+")
        gaf_out.write("!gaf-version:2.0\n")
        gaf_out.write("!%s\n" % ("\t".join(self.gaf_2_x_fields)))
        gaf_out.close()
        self.annotations[self.annotations[col_name]>th].to_csv(outfile,sep="\t",header=False, index=False,mode="a")
        return True

    def write_gaf_head(self,outfile="test.out"):
        gaf_out = open(outfile,"w")
        gaf_out.write("!gaf-version:2.0\n")
        gaf_out.write("!%s\n" % ("\t".join(self.gaf_2_x_fields)))
        gaf_out.close()

    def clear_annotations(self):
        self.annotations = pd.DataFrame()

    def add_annotation(self,in_gaf_2_x):
        in_gaf_2_x_df = pd.DataFrame.from_dict([in_gaf_2_x],"columns")
        self.annotations = self.annotations.append(in_gaf_2_x_df)

    def add_col_all(self,col_name,value):
        num_annot = len(self.annotations)
        if(num_annot==0):
            sys.stderr.write("No annotations, please add some valid data before filling in other columns\n")
            valid_cols = ", ".join([tag for tag,value in self.gaf_2_x_default.iteritems() if value == 2])
            sys.stderr.write("%s\n" % valid_cols)
        else:
            col_data = np.repeat(value,num_annot)
            col_series = pd.Series(col_data,name=col_name)
            self.add_col(col_series)

    def add_col(self,col):
        if len(self.annotations) == 0:
            self.annotations = pd.DataFrame(col)
        else:
            if col.name in self.annotations:
                self.annotations[col.name] = col
            else:
                self.annotations = pd.concat([self.annotations,col],axis=1)

    def init_annotations(self,cols):
        if len(self.annotations) > 0:
            sys.stderr.write("This GAF has already been initialized\n")
        else:
            db_object_id = pd.Series(cols["gene"],name="db_object_id")
            db_object_symbol = pd.Series(cols["gene"],name="db_object_symbol")
            term_accession = pd.Series(cols["go"],name="term_accession")
            self.annotations = pd.concat([db_object_id,db_object_symbol,term_accession],axis=1)
    def add_aspect(self,obo):
        if len(self.annotations) == 0:
            sys.stderr.write("This GAF has not been initialized\n")
        else:
            go_list = self.annotations["term_accession"]
            aspects = {"biological_process":"P","molecular_function":"F","cellular_component":"C"}
            go_aspect = {term['id']:aspects[term['namespace']] for term in obo.terms}
            aspect = [ go_aspect[go] if go in go_aspect else "N"  for go in go_list]
            aspect_series = pd.Series(aspect,name="aspect")
            self.add_col(aspect_series)
    def drop_col(self,col_name):
        self.annotations = self.annotations.drop(col_name,axis=1)

    def reorder_cols(self):
        self.annotations = self.annotations.reindex_axis(self.gaf_2_x_fields,1)
    
    gaf_2_x_fields = ["db","db_object_id","db_object_symbol","qualifier","term_accession","db_reference","evidence_code","with","aspect","db_object_name","db_object_synonym","db_object_type","taxon","date","assigned_by","annotation_extension","gene_product_form_id"]
    gaf_2_x_default = {
        "db": 1,
        "db_object_id": 2,
        "db_object_symbol": 2,
        "qualifier": 0,
        "term_accession": 2,
        "db_reference": 1,
        "evidence_code": 1,
        "with": 0,
        "aspect": 2,
        "db_object_name": 0,
        "db_object_synonym": 0,
        "db_object_type": 1,
        "taxon": 1,
        "date": 1,
        "assigned_by": 1,
        "annotation_extension": 0,
        "gene_product_form_id": 0
    }
'''
gaf_2_x_default = {
    "db": True,
    "db_object_id": True,
    "db_object_symbol": True,
    "qualifier": False,
    "term_accession": True,
    "db_reference": True,
    "evidence_code": True,
    "with": False,
    "aspect": True,
    "db_object_name": False,
    "db_object_synonym": False,
    "db_object_type": True,
    "taxon": True,
    "date": True,
    "assigned_by": True,
    "annotation_extension": False,
    "gene_product_form_id": False
}
'''
