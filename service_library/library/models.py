from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]



class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author =models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title", "author"]
    

class Reader(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        ordering = ["first_name", "last_name"]



class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Читатель')
    loan_date = models.DateTimeField(verbose_name='Выдана книга читателю', auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True, verbose_name='Возвращена читателем')


    def __str__(self):
        return f"{self.book.title} - {self.reader}"

    
    class Meta:
        ordering = ["book", "reader"]