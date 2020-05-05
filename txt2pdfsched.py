from fpdf import FPDF 
  
  
# save FPDF() class into a  
# variable pdf 
pdf = FPDF() 
  
# Add a page 
pdf.add_page() 
  
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 25) 
  
# create a cell 
pdf.cell(200, 10, txt = "Matchups",  
         ln = 1, align = 'C') 
f = open("sched.txt", "r") 
pdf.set_font("Arial", size = 11)  
# insert the texts in pdf 
line = 1
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align='L' )
    line+=1
pdf.output("schedule.pdf")    
