from datacenter.models import Schoolkid, Mark, \
                              Lesson, Commendation, Chastisement
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.commendations import commendations
import random


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
    for i, bad_mark in enumerate(bad_marks, 1):
        bad_mark.points = 5
        bad_mark.save()
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
        subject__title=subject).order_by('-date')[0]
    if not Commendation.objects.filter(created=latest_lesson.date,
                                       schoolkid=schoolkid,
                                       subject=latest_lesson.subject,
                                       teacher=latest_lesson.teacher):
        Commendation.objects.create(
            text=random.choice(commendations),
            created=latest_lesson.date,
            schoolkid=schoolkid,
            subject=latest_lesson.subject,
            teacher=latest_lesson.teacher)
        print('Похвала для {} - добавлена.'.format(full_name))
    else:
        print('Похоже, что похвала для последнего урока {} - уже есть.'.format(
            subject))


if __name__ == "__main__":
    pass
