# Variable in Python
## 1. Comment trong Python
- Có 2 cách để comment trong python:
  - C1: Sử dụng dấu `#` để comment 1 dòng.
  - C2: Sử dụng dấu `"nội dung comment"` ==> ít sử dụng do tùy thuộc vào HĐH hoặc phiên bản.

## 3. Khai báo biến
 Để khai báo biến sử dụng cú pháp:
 ```
 tenbien=giá trị
 ```
Ví dụ:
 ```
name = 'Nguyen Van A'
 ```
`Note`
 ```
Biến không chứa chữ số đầu tiên (ex:124_bien)
Biến không chứa space (ex: Ten bien)
Biến không có dấu  
 ```
## 4. Toán tử
Python cũng có các toán tử tương tự các ngôn ngữ khác

## 5. Data Type
  - Kiểu số - Number
  - Kiểu chuỗi - String
  - Kiểu bộ - Tuple
  - Kiểu Danh sách - list
  - Từ điển - dictionary
  - None

## 6. String
Python has three different ways to accomplish string formatting:
```
    - Using the % method
    - Using .format()
    - using formatted string literals (f-string)
```
To concatenate (ket noi) string:
```
    - Use +
    - Use .join() method
```
String slicing
```
    my_string[0:4]: grad characters 0-3
```
## 7. Numeric
Các kiểu số:
```
  - int
  - float
  - complex
 ```
## 8. Kiểu List
### Create List
Các cách tạo một List:
```
- Khởi tạo một List empty: []
- Khởi tạo List có các thành phần ngăn cách bới dấu ',' : [1,2,3]
- Sử dụng list() function
```
### List Methods
```
- append()
- clear()
- copy()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()
- sort()
```
#### Adding to a List
```
  - append(): add item to the end of a pre-existing list
  - extend(): sử dụng để thêm list vào 1 list khác
  - insert(): thêm item vào vị trí mong muốn. Ex: my_list.insert(0, 'first'): thêm 'first' vào vị trí 0
```
#### Delete from a List
```
  - clear(): remove everyhing from the list
  - pop(): 
  - remove(): xóa phần tử đầu tiên giống với giá trị truyền vào
  - del
```
## 9. Tuples
### Khái niệm
Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số). Còn lại thì cách lưu trữ của nó cũng khá giống như kiểu dữ liệu list
### Khai báo
Có nhiều cách để khai báo một Tuple:
```
>>> a_tuple = 4,5
or
>>> a tuple = (2,3,4)
```
### Làm việc với Tuple
Nếu dùng **dir(tuple())** ta có 2 phương thức là **count()** và **index()**

**count()** dùng để find có bao nhiêu phần tử match với value truyền vào. ex:
```
>>> a_tuple = (1,2,3,3)
>>> a_tuple.count(3)
2
```
**index()** tìm kiếm index đầu tiên có giá trị bằng value truyền vào. EX:
```
>>> a_tuple = (1,2,3,3)
>>> a_tuple.index(2)
1
```


