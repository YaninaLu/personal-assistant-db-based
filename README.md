To work with contacts type in:
~~~
-a add/change -t contact --name "Name Surname" --birthday dd.mm.yyyy --phone 1234567890/+123456789011 
--email blabla@mail.com --address "12 Road City Country"

-a remove -t contact --name "Name Surname"

-a search -t contact --name "Name Surname" --phone 1234567890/+123456789011 --email blabla@mail.com
~~~

To work with notes type in:
~~~
-a add/change -t note --title "Title" --text "Text" --tags "tag1 tag2 tag3"

-a remove -t note --title "Title"

-a search -t note --title "Title" --text "Text" --tags "tag"
~~~