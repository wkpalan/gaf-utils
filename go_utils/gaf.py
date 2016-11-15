import re, sys
import pandas as pd

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


    def write_gaf(self,outfile):
        self.annotations = self.annotations.reindex_axis(self.gaf_2_x_fields,1)
        gaf_out = open(outfile,"w+")
        gaf_out.write("!gaf-version:2.0\n")
        gaf_out.write("!%s\n" % ("\t".join(self.gaf_2_x_fields)))
        #out_lines = []
        #out_lines.append()
        self.annotations.to_csv(outfile,sep="\t",header=False, index=False,mode="a")
        # for annot in self.annotations:
        #     annot_values = [annot.get(k) for k in self.gaf_2_x_fields]
        #     gaf_out.write("%s\n" % ("\t".join(annot_values)))
        # gaf_out.close()

    def write_gaf_head(self,outfile):
        self.annotations = self.annotations.reindex_axis(self.gaf_2_x_fields,1)
        gaf_out = open(outfile,"w")
        gaf_out.write("!gaf-version:2.0\n")
        gaf_out.write("!%s\n" % ("\t".join(self.gaf_2_x_fields)))
        gaf_out.close()

    def clear_annotations(self):
        self.annotations = pd.DataFrame()

    def add_annotation(self,in_gaf_2_x):
        in_gaf_2_x_df = pd.DataFrame.from_dict([in_gaf_2_x],"columns")
        self.annotations = self.annotations.append(in_gaf_2_x_df)

    # def get_sections(self,lines):
    #     """
    #     Separates an obo file into stanzas and process.
    #     Returns (typedefs, terms, instances, header) tuples
    #     where `typedefs`, `terms`, and `instances` are lists of
    #     dictionaries and `header` is a dictionary.
    #     """
    #     typedefs, terms, instances = [], [], []
    #     groups = itertools.groupby(lines, lambda line: line.strip() == '')
    #     for is_blank, stanza_lines in groups:
    #         if is_blank:
    #             continue
    #         stanza_type_line = next(stanza_lines)
    #         stanza_lines = list(stanza_lines)
    #         if stanza_type_line.startswith('[Typedef]'):
    #             typedef = self.parse_stanza(stanza_lines, self.typedef_tag_singularity)
    #             typedefs.append(typedef)
    #         elif stanza_type_line.startswith('[Term]'):
    #             term = self.parse_stanza(stanza_lines, self.term_tag_singularity)
    #             terms.append(term)
    #         elif stanza_type_line.startswith('[Instance]'):
    #             instance = self.parse_stanza(stanza_lines, self.instance_tag_singularity)
    #             instances.append(instance)
    #         else:
    #             stanza_lines = [stanza_type_line] + stanza_lines
    #             header = self.parse_stanza(stanza_lines, self.header_tag_singularity)
    #     return typedefs, terms, instances, header
    #
    # # regular expression to parse key-value pair lines.
    # tag_line_pattern = re.compile(
    #     r'^(?P<tag>.+?): *(?P<value>.+?) ?(?P<trailing_modifier>(?<!\\)\{.*?(?<!\\)\})? ?(?P<comment>(?<!\\)!.*?)?$')
    #
    # def parse_tag_line(self,line):
    #     """
    #     Take a line representing a single tag-value pair and parse
    #     the line into (tag, value, trailing_modifier, comment).
    #     """
    #     match = re.match(self.tag_line_pattern, line)
    #     if match is None:
    #         print('Tag-value pair parsing failed for', line)
    #         raise ValueError
    #     tag = match.group('tag')
    #     value = match.group('value')
    #     trailing_modifier = match.group('trailing_modifier')
    #     if trailing_modifier:
    #         trailing_modifier = trailing_modifier.strip('{}')
    #     comment = match.group('comment')
    #     if comment:
    #         comment = comment.lstrip('! ')
    #     return tag, value, trailing_modifier, comment
    #
    # def parse_stanza(self,lines, tag_singularity):
    #     """
    #     Returns a dictionary representation of a stanza.
    #     """
    #     stanza = dict()
    #     for line in lines:
    #         if line.startswith('!'):
    #             continue
    #         tag, value, trailing_modifier, comment = self.parse_tag_line(line)
    #         if tag_singularity.get(tag, False):
    #             stanza[tag] = value
    #         else:
    #             stanza.setdefault(tag, []).append(value)
    #     return stanza

    gaf_2_x_fields = ["db","db_object_id","db_object_symbol","qualifier","term_accession","db_reference","evidence_code","with","aspect","db_object_name","db_object_synonym","db_object_type","taxon","date","assigned_by","annotation_extension","gene_product_form_id"]
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
