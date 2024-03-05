import cmd

class Node:
	def __init__(self, *nums):
		self.__n, *nums = nums
		self.__l = None
		self.__r = None

		for n in nums:
			self.append(n)

	def append(self, *ns):
		for n in ns:
			if n <= self.__n:
				if self.__l == None: 
					self.__l = Node(n)
				else:
					self.__l.append(n)
			else:
				if self.__r == None: 
					self.__r = Node(n)
				else:
					self.__r.append(n)

	def val(self): return self.__n

	def pre_order(self):
		order = []
		order.append(self.__n)
		if self.__l != None:
			order += self.__l.pre_order()
		if self.__r != None:
			order += self.__r.pre_order()
		return order

	def in_order(self):
		order = []
		if self.__l != None:
			order += self.__l.in_order()
		order.append(self.__n)
		if self.__r != None:
			order += self.__r.in_order()
		return order

	def post_order(self):
		order = []
		if self.__l != None:
			order += self.__l.post_order()
		if self.__r != None:
			order += self.__r.post_order()
		order.append(self.__n)
		return order
	   
	def contains(self, n):
		if self.__n == n:
			return True
		elif self.__l != None and n <= self.__n:
			return self.__l.contains(n)
		elif self.__r != None and n >  self.__n:
			return self.__r.contains(n)
		else:
			return False

	def rows(self, depth=0, rows=None):
		if rows is None:
		    rows = []
		
		if len(rows) <= depth:
		    rows.append([])
		
		rows[depth].append(self.__n)
		if self.__l != None:
			self.__l.rows(depth+1, rows)
		else: 
			rows[depth].append(None)

		if self.__r != None:
			self.__r.rows(depth+1, rows)
		else: 
			rows[depth].append(None)
		
		return rows

	def __repr__(self):
		return f"{self.__n}({self.__l or '_'} {self.__r or '_'})"

class BinaryTreeCLI(cmd.Cmd):
	prompt = ' >> '
	tree = None
	
	def __parse(self, line):
		return [int(s.strip()) for s in line.split(',') if s]
	
	def postcmd(self, stop, line):
		if self.tree: print(self.tree)
		else: print("No tree initialised")
		return 

	def cmdloop(self, intro=None):
		print(intro)
		while True:
			try:
				super().cmdloop(intro="")
				break
			except KeyboardInterrupt:
				print("^C")
				exit(0)
	
	def do_new(self, line):
		"""Initialise the tree"""
		try:
			self.tree = Node(*self.__parse(line))
		except:
			print("Tree needs numbers.")
		
	def do_show(self, _):
		"""Visualise the tree"""
		print(self.tree)
	
	def do_preorder(self, _):
		"""Show pre-order"""
		if self.tree: print(self.tree.pre_order())
	
	def do_inorder(self, _):
		"""Show in-order"""
		if self.tree: print(self.tree.in_order())
	
	def do_postorder(self, _):
		"""Show post-order"""
		if self.tree: print(self.tree.post_order())
	
	def do_push(self, line):
		"""Push items to the tree"""
		try:
			self.tree.append(*self.__parse(line))	
		except:
			print("Tree needs numbers.")
	
	def do_contains(self, item):
		"""Give an item and check if it is in the tree."""
		try:
			print(self.tree.contains(int(item)))
		except:
			print("Give a single number.")


if __name__ == '__main__':
	t = Node(40, 30, 50, 25, 35, 45, 60, 15, 28, 55, 70)
	print( t.rows())
	# BinaryTreeCLI().cmdloop("TREES. Type 'help' if needed.")
