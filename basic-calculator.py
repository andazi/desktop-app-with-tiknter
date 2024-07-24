from tkinter import *
import ast
import operator as op

root = Tk()

# title 
root.title("Basic Calculator")

e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# define functions
def add_btn(value):
	# concat value in front of value
	current_val = e.get()
	# delete previous value and replace with new value
	e.delete(0,END)
	return e.insert(0, str(current_val) + str(value))
	
def sign_btn(value):
	# concat value in front of value
	current_val = e.get()
	# delete previous value and replace with new value
	e.delete(0,END)
	return e.insert(0, str(current_val) + " " + str(value) + " ")

def clear_btn():
	e.delete(0, END)
	
def submit():
	entry_expr = e.get()
	
	operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
}
	
	def eval_expr(expr):
		def eval_(node):
		    if isinstance(node, ast.Num):  # <number>
		        return node.n
		    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
		        left = eval_(node.left)
		        right = eval_(node.right)
		        return operators[type(node.op)](left, right)
		    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
		        operand = eval_(node.operand)
		        return operators[type(node.op)](operand)
		    else:
		        raise TypeError(node)
		
		node = ast.parse(expr, mode='eval').body
		return eval_(node)
	result = eval_expr(entry_expr)
	# display result
	e.delete(0, END)
	e.insert(0, result)

# define buttons

btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_btn(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_btn(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_btn(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_btn(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_btn(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_btn(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_btn(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_btn(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_btn(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_btn(0))

btn_clear = Button(root, text="C", padx=40, pady=20, command=clear_btn)
btn_div = Button(root, text="/", padx=40, pady=20, command=lambda: sign_btn("/"))
btn_prod = Button(root, text="*", padx=40, pady=20, command=lambda: sign_btn("*"))
btn_sub = Button(root, text="-", padx=40, pady=20, command=lambda: sign_btn("-"))
btn_add = Button(root, text="+", padx=40, pady=20, command=lambda: sign_btn("+"))
btn_submit = Button(root, text="=", padx=40, pady=20, command=submit)

# add buttons to screen

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_0.grid(row=4,column=0)

btn_clear.grid(row=1,column=3)
btn_div.grid(row=2,column=3)
btn_prod.grid(row=3,column=3)
btn_sub.grid(row=4,column=3)
btn_add.grid(row=4,column=2)
btn_submit.grid(row=4,column=1)
































root.mainloop()
