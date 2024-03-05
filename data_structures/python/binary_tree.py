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
	
	def do_contains(self, line):
		

if __name__ == '__main__':
	BinaryTreeCLI().cmdloop("TREES. Type 'help' if needed.")
