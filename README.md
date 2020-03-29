# How to adjust school journal

```fix_marks(full_name)``` - based on input name, function replacing 2 or 3 point degree with 5;
```remove_chastisements(full_name)```  - based on input name, removing all assigned chastisements;
```create_commendation(full_name, subject)``` - based on input name and desired subject, script is adding the random commendation into the last lesson;

If script couldn't locate inserted name, or the name is assigned to multiply rows, respected alerts will be printed. 

Interaction with the script via Django shell:
```python manage.py shell```

# Examples

First step is to load all necessary functions:
```from scripts import fix_marks, remove_chastisements, create_commendation```

Then, you can run fuctions:

```fix_marks('Калинина Марфа')```
output:
```263 оценок исправлено для ученика Калинина Марфа.```

```remove_chastisements(full_name)```
output:
```Удалены все замечания для ученика Калинина Марфа.'```

```create_commendation('Калинина Марфа', 'Музыка')```
output:
```Похвала для Калинина Марфа - добавлена.```


# Notes
The code is written for educational purposes - this is a lesson in the Python and web development course at [Devman] (https://dvmn.org).