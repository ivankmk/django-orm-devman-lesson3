from datacenter.models import Schoolkid, Mark, \
                              Lesson, Commendation, Chastisement
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.commendations import commendations
import random


def get_random_commendation():
    return random.choice(commendations)


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print('There is no kid with name {}'.format(full_name))
        return None
    except MultipleObjectsReturned:
        print('There are multiple kids with name {}'.format(full_name))
        return None
    return schoolkid


def fix_marks(full_name):
    schoolkid = get_schoolkid(full_name)
    bad_marks = Mark.objects.filter(
        points__in=[2, 3], schoolkid=schoolkid)
    i = 0
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
        i += 1
    print('{} оценок исправлено для ученика {}.'.format(i, full_name))


def remove_chastisements(full_name):
    schoolkid = get_schoolkid(full_name)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
    print('Удалены все замечания для ученика {}.'.format(full_name))


def create_commendation(full_name, subject):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None
    latest_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject).order_by('date')[0]
    Commendation.objects.create(
        text=get_random_commendation(),
        created=latest_lesson.date,
        schoolkid=schoolkid,
        subject=latest_lesson.subject,
        teacher=latest_lesson.teacher)
    print('Похвала для {} - добавлена.'.format(full_name))


if __name__ == "__main__":
    pass
