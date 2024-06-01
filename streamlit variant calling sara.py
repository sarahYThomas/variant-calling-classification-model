import streamlit as st
import pickle
import pandas as pd
#setting the interface 
st.title('conflicating variant calling classification ')
st.info('web page for cfvar classification')
st.sidebar.header('Features')
#assigned faeatures columns to our streamlit app
chromosome=st.text_input('CHROM')
variant_postion_onchromosome=st.text_input('POS')
refernce_form=st.text_input('REF')
alternative_form= st.text_input('ALT')
Allele_frequencies_ESP = st.text_input('AF_ESP')
Allele_frequencies_EXAC=st.text_input('AF_EXAC')
Allele_frequencies_TGP=st.text_input('AF_TGP')
Allele_frequencies_genome_pro=st.text_input('CLNDN')
top_level_expression = st.text_input('CLNHGVS') 
Variant_Type=st.text_input('CLNVC')
Allele_origin=st.text_input('ORIGIN')
Allele =st.text_input('Allele')
Consequence=st.text_input('Consequence')
IMPACT=st.text_input('IMPACT')
gene_SYMBOL=st.text_input('SYMBOL')
Feature_type=st.text_input('Feature_type')
BIOTYPE=st.text_input('BIOTYPE')
cDNA_position=st.text_input('cDNA_position')
CDS_position =st.text_input('CDS_position')
Protein_position=st.text_input('Protein_position')
Amino_acids=st.text_input('Amino_acids')
Codons = st.text_input('Codons')
dna_strand = st.text_input('STRAND')
Loss_of_Function_tolerance= st.text_input('LoFtool')
CADD_PHRED= st.text_input('CADD_PHRED')
Allele_Freq_Mean= st.text_input('Allele_Freq_Mean')
Pathogenicity_Score_Mean= st.text_input('Pathogenicity_Score_Mean')
#creating dataform
df=pd.DataFrame({'CHROM':[chromosome],'POS':[variant_postion_onchromosome],
'REF':[refernce_form], 'ALT':[alternative_form],
'AF_ESP':[Allele_frequencies_ESP],'AF_EXAC':[Allele_frequencies_EXAC],'AF_TGP':[Allele_frequencies_TGP],
'CLNDN':[Allele_frequencies_genome_pro],'CLNHGVS':[top_level_expression],'CLNVC':[Variant_Type],'ORIGIN':[Allele_origin],
'Allele':[Allele],'Consequence':[Consequence],
'IMPACT':[IMPACT] , 'SYMBOL':[gene_SYMBOL],'Feature_type':[Feature_type],'BIOTYPE':[BIOTYPE] , 'cDNA_position':[cDNA_position]
 ,'CDS_position':[CDS_position],
'Protein_position':[Protein_position] , 'Amino_acids':[Amino_acids] ,'Codons':[Codons] ,'STRAND':[dna_strand] , 'LoFtool':[Loss_of_Function_tolerance] ,
'CADD_PHRED':[CADD_PHRED], 'Allele_Freq_Mean':[Allele_Freq_Mean] , 'Pathogenicity_Score_Mean':[Pathogenicity_Score_Mean]},index=[0])
#load our previously implementated model 
model=pickle.load(open(r"C:\Users\Dell\Downloads\machine_model_1.sav",'rb'))
Confirmation=st.sidebar.button('confirm')
if Confirmation:
    result=model.predict(df)
    st.write(result)