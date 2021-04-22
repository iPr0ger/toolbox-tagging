from django.db import models

# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Resource types"


class ResearchField(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Research fields"


class SpecificTopic(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specific topics"


class GeographicalScope(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Geographical scope"


class CountryGrouping(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    geographical_scope = models.ForeignKey(GeographicalScope, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries grouping"


class DataType(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Data Types"


class DataTypeSub(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Data types subgroups"


class StageInDS(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stage in data sharing life cycle"