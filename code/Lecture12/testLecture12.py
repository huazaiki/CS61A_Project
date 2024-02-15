states = {
	"CA": "California",
	"DE": "Delaware",
	"NY": "New York",
	"TX": "Texas",
	"WY": "Wyoming"
}

def matrix(rows, cols):
    """初始化矩阵，矩阵元素的值初始为 0 """
    return [ [0 for col in range(cols)] for row in range(rows) ]

def value(matrix, row, col):
    return matrix[row][col]

def set_value(matrix, row, col, val): 
    matrix[row][col] = val

def f():
    assert 1 == False, 'branches must be trees'

if __name__ == '__main__':
    print(f())


