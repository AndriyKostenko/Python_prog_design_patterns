from abc import abstractmethod, ABC

# SINGLE-RESPONSIBILITY INTERFACES
class Printer(ABC):
	@abstractmethod
	def print(self, document):
		pass


class Scanner(ABC):
	@abstractmethod
	def scan(self, document):
		pass 


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class OldFashionedPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")


class MultiFunctionDevice(Printer, Scanner, Fax):
	pass 


class MultiFunctionMachine(MultiFunctionDevice):
	def __init__(self, printer: Printer, scanner: Scanner, fax: Fax):
		self.printer = printer
		self.scanner = scanner
		self.fax = fax

	def print(self, document):
		self.printer.print(document)

	def scan(self, document):
		self.scanner.scan(document)




		