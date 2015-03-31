from django.db import models

# Create your models here.
class KeyCombo(models.Model):
    shift = models.BooleanField(default=False, blank=True)
    alt = models.BooleanField(default=False, blank=True)
    ctrl = models.BooleanField(default=False, blank=True)
    meta = models.BooleanField(default=False, blank=True)
    keychar = models.CharField(max_length=10)
    meaning = models.CharField(max_length=50)

    def __unicode__(self):
        shift = alt = ctrl = meta = ""
        if self.shift:
            shift = 'shift + '
        if self.alt:
            alt = 'alt + '
        if self.ctrl:
            ctrl = 'ctrl + '
        if self.meta:
            meta = 'meta + '
        return u"{}".format(shift + alt + ctrl + meta + self.keychar)