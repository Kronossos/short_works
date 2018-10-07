#!/usr/bin/python2
# -*- coding: utf-8 -*-
import random
from fpdf import FPDF

vowels = ["a","o","i","u","e"]
consonants = raw_input("Enter the range of consonants (np.> d s r t) >").split()

pages=int(raw_input("Enter the number of pages >"))

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

for quantity in xrange(pages*80):
    pdf.cell(20, 30, random.choice(consonants)+random.choice(vowels))
    if (quantity+1)%10==0: pdf.ln()

pdf.output('Hiragana exercises.pdf')
