# Purpose of the script
To have an ability to adjust the assingment grades, remove chastisements and create commendation in the school journal.

# How to adjust school journal

```python
fix_marks(full_name)
```
- based on the input name, function will replace point 2 or 3 with 5;

```python
remove_chastisements(full_name)
```  
- based on the input name, all assigned chastisements will be removed;


```python
create_commendation(full_name, subject)
``` 
- based on the input name and desired subject, script will add the random commendation into the last lesson;

If script couldn't locate the inserted name, or the name was assigned to multiply rows, respected alerts will be printed. 

To interact with the script could be used Django shell:

```python manage.py shell```

# Examples

First step is to load all necessary functions:
```from scripts import fix_marks, remove_chastisements, create_commendation```

Then, you can run fuctions:

```python
fix_marks('Калинина Марфа')
```
output:
```263 оценок исправлено для ученика Калинина Марфа.```


```python
remove_chastisements(full_name)
```
output:
```Удалены все замечания для ученика Калинина Марфа.```

```python
create_commendation('Калинина Марфа', 'Музыка')
```

output:
```Похвала для Калинина Марфа - добавлена.```


# Notes
The code is written for educational purposes - this is a lesson in the Python and web development course at [Devman](https://dvmn.org).