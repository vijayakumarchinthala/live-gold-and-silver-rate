# Import Required library
from bs4 import BeautifulSoup
import requests
from tkinter import *
from datetime import date
from tkinter import ttk
from PIL import Image, ImageTk

# Extract Integer or Float from String
def get_number_from_string(string):
	return float(''.join([x for x in string if x.isdigit() or x == '.']))


# Returns the current local date
today = date.today()


# method to get the price of silver
def silver_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/silver-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding meta info for the current price
	price = soup.find("div", class_="gold_silver_table right-align-content").find(
		"tr", class_="odd_row").findAll("td")

	# returning the price in text
	return price[1].text


# method to get the price of gold
def gold_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/gold-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding meta info for the current price
	price = soup.find("div", class_="gold_silver_table right-align-content").find(
		"tr", class_="odd_row").findAll("td")

	# returning the price in text
	return price[1].text


# Get price for a particular weight
def change_price(weight_value):

	g_price1 = float(weight_value)*get_number_from_string(gold_price())
	s_price1 = float(weight_value)*get_number_from_string(silver_price())
	g_price = round(g_price1+(g_price1*0.03),2)
	s_price = round(s_price1+(s_price1*0.03),2)

	silver_price_label.config(text=f"{s_price} Rs")
	gold_price_label.config(text=f"{g_price} Rs")


# Create Object
root = Tk()

# Set Geometry
root.geometry("600x700")
root.title("GOLD RATES")

# Create an object of tkinter ImageTk
image1= ImageTk.PhotoImage(Image.open(r"picture1.png"))

# Create a Label Widget to display the text or Image
Label(root, image = image1).pack()


#Create Label
Label(root, text="SRI GOWRI SHANKAR JEWELLERY", font=(
	"Helvetica 15 bold"), fg="blue", bg="orange").pack()
#Create Label
Label(root, text="CHINNA BAZAAR,NELLORE", font=(
	"Helvetica 10 bold"), fg="blue",bg="orange").pack()

# Create Label
Label(root, text="GOLD AND SILVER PRICE INDIA", font=(
	"Helvetica 15 bold"), fg="blue").pack()

# Frame1
frame1 = Frame(root)
frame1.pack(pady=20)

Label(frame1, text="Today Date:- ", font=("Helvetica 15 bold")).pack(side=LEFT)
Label(frame1, text=today, font=("Helvetica 15")).pack()


# Frame2
frame2 = Frame(root)
frame2.pack(pady=20)

# Set Variable
variable = StringVar(root)
variable.set("1")

Label(frame2, text="Select Weight:- ",
	font=("Helvetica 15 bold")).pack(side=LEFT)
w = OptionMenu(frame2, variable, "1", "8", "100",
			"500", "1000", command=change_price)
w.pack(side=LEFT)
Label(frame2, text="gm", font=("Helvetica 15")).pack(side=LEFT)


# Frame3
frame3 = Frame(root)
frame3.pack()

Label(frame3, text="Silver Price:- ", font=("Helvetica 15 bold")).pack(side=LEFT)
silver_price_label = Label(frame3, text="", font=("Helvetica 15"))
silver_price_label.pack(pady=20)


# Frame4
frame4 = Frame(root)
frame4.pack()

Label(frame4, text="Gold Price (22CT):- ", font=("Helvetica 15 bold")).pack(side=LEFT)
gold_price_label = Label(frame4, text="", font=("Helvetica 15"))
gold_price_label.pack(pady=20)

#Create Label
Label(root, text="AUTHOR: Chinthala Vijaya Kumar", font=(
	"Helvetica 10 bold"), fg="blue",bg="orange").pack()
# Execute Tkinter
root.mainloop()
