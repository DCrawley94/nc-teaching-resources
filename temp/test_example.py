from unittest.mock import Mock


mock = Mock()
mock.side_effect = [1,2,3,4,5]
mock.return_value = 10


print(mock())

print(mock())

print(mock())

print(mock())

print(mock())

print(mock())