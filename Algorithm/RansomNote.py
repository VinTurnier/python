"""
	Ransom Note takes in a magazine string and a note string 
	to know if we can build a ransom note the words in the magazine
	has to equal or be more then that in the note

"""

class RansomNote(object):

	def __init__(self,note: str, magazine: str):

		self.note = note.split(' ')
		self.magazine = magazine.split(' ')

	def getStringFreq(self, string):
		# gathers the frquency of the words 
		# using dictionaries 
		string_dict = dict.fromkeys(string,0)
		for word in string:
			string_dict[word]+=1

		return string_dict

	def hasEnoughString(self,magazine_freq, note_freq):
		# here we want to do two things
		# 1) check to see if the same key are not present
		# 2) if it is the same key check to see if the frequency is greater then
		# if any of these assumptions are true return false
		for key, value in note_freq.items():
			if (key not in magazine_freq) or magazine_freq[key]<value:
				return False
		return True
		
	

	def canBuildRansomNote(self):
		# first we want to add the notes in a dictionary
		magazine_freq = self.getStringFreq(self.magazine)
		note_freq = self.getStringFreq(self.note)
		return self.hasEnoughString(magazine_freq,note_freq)


if __name__== "__main__":
	note = "I will take care of it"
	magazine = "I will take care of it nice nice"
	rn = RansomNote(note,magazine)
	print(rn.canBuildRansomNote())