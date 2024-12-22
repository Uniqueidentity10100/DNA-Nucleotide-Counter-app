import pandas as pd
import streamlit as st
import altair as at
from PIL import Image

url = "https://raw.githubusercontent.com/Uniqueidentity10100/DNA-Nucleotide-Counter-app/main/dna-163466_640.webp"
response = requests.get(url)
images = Image.open(BytesIO(response.content)st.image(images, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App
         
  This app counts the Number of Nucleotide Composition
         
  ***            
          """)
st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence =st.text_area("Sequence Input",sequence_input,height=250)
sequence =sequence.splitlines()
sequence=sequence[1:]
sequence=' '.join(sequence)

st.write("""
***
         """)

st.header('INPUT(DNA Query)')
sequence
st.header('OUTPUT (DNA Nucleotide Count)')
st.subheader('1. Print dictionary')
def DNA_count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d
Count = DNA_count(sequence)

st.subheader('2. Print text')
st.write('There are '+str(Count['A'])+' adenine (A)')
st.write('There are '+str(Count['T'])+' thymine (T)')
st.write('There are '+str(Count['G'])+' guanine (G)')
st.write('There are '+str(Count['C'])+' cytosine(C)')

st.subheader('3. Display Data Frame')
df=pd.DataFrame.from_dict(Count,orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = at.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=at.Step(80)  
)
st.write(p)
