# progress bar across rounds
There are two ways of doing it.
one is compact and it uses oTree internal fields so there is no warranty it will function in next releases
another one is more lengthy, but the right way to do it.

If you insert the bar to ALL pages I would consider to create your own Page class
and then inherit all your pages in the app from this new Page class.
Like

```python
class MyPage(Page):

  def vars_for_template(self):
      return{
             'progressrel':progress(self)
             }

class Demographics(MyPage):
    ...

class BigFive(MyPage):
   ...
```
