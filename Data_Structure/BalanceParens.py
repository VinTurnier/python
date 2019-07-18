from Stack import Stack

class BalanceParens(object):


	def __init__(self):
		self.stack = Stack()
		self.items = ["[","(","{"]
		

	def solution(self, paren_string_list):
		"""
			paren_string_list = List[char]
		"""
		for i in range(len(paren_string_list)):
			if paren_string_list[i] in self.items:
				self.stack.push(paren_string_list[i])
			
			else:
				if (paren_string_list[i] == ')' and self.stack.peek() != '(')\
					or (paren_string_list[i] == '}' and self.stack.peek() != '{')\
					or (paren_string_list[i] == ']' and self.stack.peek() != '['):
					return False
				else:
					self.stack.pop()

		return self.stack.isEmpty()


if __name__=="__main__":
	string = ['{','(',')','[','{','(','{','}',')','[',']','(',')','}',']','(','[',']',')','}']
	bp = BalanceParens()
	print(bp.solution(string))
