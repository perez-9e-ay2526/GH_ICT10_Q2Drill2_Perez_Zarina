# Set Operators

from pyscript import display, document


member_names = {'Zarina Perez', 'Maryam Ledesma', 'Nathan Bautista', 'Hans Baquiran', 'Aiva Suson', 'Zoey Reyes', 'Oshri Gonzales', 'Rico Gozum', 'Renzo Madrono', 'David Valeriano', 'Jamielle Orduna', 'Alyssandra Rodriguez', 'Cyanne Leachon', 'Ramon Santiago', 'Thea Correa', 'Reign Macachor', 'Franco Garcia', 'Ethan Valerio'}

display(*sorted(member_names), target='result')
document.getElementById('total').innerHTML = len(member_names)

def confirm_member(e):
    global member_names

    document.getElementById('result').innerHTML = ''

    #turns input into a set
    input_first = str(document.getElementById('firstname').value) 
    input_last = str(document.getElementById('lastname').value)

    input_full = str(input_first) + " " + str(input_last)

    input_final = {input_full.title()}

    #unites the member names and the input
    member_names |= input_final

    display(*sorted(member_names), target ='result') 

    #displays the numnber of club members
    document.getElementById('total').innerHTML = len(member_names)
