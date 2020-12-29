from django.db import models


class Admin(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    website = models.URLField()
    location = models.CharField(max_length=20)
    twitter = models.URLField()
    insta = models.URLField()
    github = models.URLField()
    linkedIn = models.URLField()
    roles = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Experience(models.Model):
    exp_types = [('Intern', 'Intern'), ('', '')]
    exp_type = models.CharField(max_length=6, choices=exp_types, default='')
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.company_name}-{self.position}-{self.duration}({self.exp_type})"


class Description(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Project(models.Model):
    proj_category = models.CharField(
        max_length=10, choices=[('All', 'all'), ('App', 'app'), ('Web', 'web')], default='all')
    proj_name = models.CharField(max_length=30)
    gitRepoLink = models.URLField()

    def __str__(self):
        return f'{self.proj_name} => {self.gitRepoLink}'


class Skill(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_val = models.IntegerField()

    def __str__(self):
        return f'{self.skill_name}-{self.skill_val}'


class About(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)
    aboutHeader = models.CharField(max_length=255)
    aboutItalic = models.CharField(max_length=255)
    aboutPara = models.CharField(max_length=255)

    def __str__(self):
        return f"About"
