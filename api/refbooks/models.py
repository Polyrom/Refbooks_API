from django.db import models


class ReferenceBook(models.Model):
    code = models.CharField(max_length=100, unique=True,
                            null=False, blank=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.code


class ReferenceBookVersion(models.Model):
    reference_book = models.ForeignKey(ReferenceBook,
                                       on_delete=models.CASCADE)
    version = models.CharField(max_length=50, null=False, blank=False)
    start_date = models.DateField(blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['reference_book', 'version'],
                name='unique_version'
            ),
            models.UniqueConstraint(
                fields=['reference_book', 'start_date'],
                name='unique_date'
            )
        ]

    def __str__(self):
        return self.version


class ReferenceBookItem(models.Model):
    reference_book_version = models.ForeignKey(ReferenceBookVersion,
                                               on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True,
                            null=False, blank=False)
    value = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.code
