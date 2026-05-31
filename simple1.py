
def greet(name: str = "World") -> str:
	"""Return a greeting for the given name."""
	return f"Hello, {name}!"


if __name__ == "__main__":
	# simple CLI: print greeting for provided name or default
	import sys
	name = sys.argv[1] if len(sys.argv) > 1 else None
	print(greet(name or "World"))
