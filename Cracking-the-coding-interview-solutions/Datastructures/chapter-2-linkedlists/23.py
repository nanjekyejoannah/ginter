def delete(self, data):
	    current = self.head
	    previous = None
	    found = False
	    while current and found is False:
	        if current.get_data() == data:
	            found = True
	        else:
	            previous = current
	            current = current.get_next()
	    if current is None:
	        raise ValueError("Data not in list")
	    if previous is None:
	        self.head = current.get_next()
	    else:
	        previous.set_next(current.get_next())
