
import numpy
import copy
import tradeup
from data import *

class backend:

	#for full-clear
	def __init__(self):
		#leere Materialliste erstellen und 5x in Itemliste kopieren
		emptyMat = [0,0,0,0,0,0,0]
		self.item = [emptyMat[:] for i in mats]
		self.total = copy.deepcopy(self.item)


	#clear current item
	def clearItem(self):
		emptyMat = [0,0,0,0,0,0,0]
		self.item = [emptyMat[:] for i in mats]

	def addItem(self):
		self.total = numpy.add(self.total, self.calc())
		return self.total

	def calc(self):
		result = copy.deepcopy(self.item)

		for matlist in result:
			for i in range(6,0,-1):
				matlist[i-1] += matlist[i]
			for i in range(7):
				matlist[i] = matlist[i]*multable[i+2]
		self.total = result
		return result

	def remaining(self):
		result = []
		for matlist in self.item:
			result.append(tradeup.remainingGather(matlist))
		self.total = result

	def addmat(self, tier, mat, btnref):
		self.item[mat][tier] += 1
		btnref["text"] = self.item[mat][tier]


	def submat(self, tier, mat, btnref):
		self.item[mat][tier] -= 1
		btnref["text"] = self.item[mat][tier]
		
	def getHumanString(self):
		result = ""
		
		for i in range(5):
			matstr = mats[i]
			result = result + matstr+"\n"
			for j in range(7):
				if(self.total[i][j] != 0):
					temp = "\t%dx %s %s\n" % (self.total[i][j], names[matstr][j+2], rawsuff[matstr])
					result += temp		
		return result
