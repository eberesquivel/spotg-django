from django.db import models


class Augment_Type(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.type)

    class Meta:
        db_table = "augment_type"


class Augment_Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    type = models.ForeignKey(Augment_Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "augment_attribute"


class Augment_Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    max_lvl = models.IntegerField()
    type = models.ForeignKey(Augment_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    attribute = models.ForeignKey(Augment_Attribute, on_delete=models.CASCADE, null=True)

    @property
    def db_values(self):
        atributo = self.attribute_id * 65536
        skill_id = self.id
        skill_max_lvl = self.max_lvl
        return "{0}\t{1}\t{2}".format(atributo, skill_id, skill_max_lvl)

    @property
    def short_format(self):
        id_skill = self.id
        skill_name = self.name[11:]
        type = self.type.type.title()
        return "{0} - {1} {2}".format(id_skill, type, skill_name)

    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)

    class Meta:
        db_table = "augment_skill"


class Reporte(models.Model):
    id = models.IntegerField(primary_key=True)
    augment_skill_id = models.CharField(max_length=70)
    attribute_description = models.TextField()

    def __str__(self):
        return str(self.augment_skill_id)
