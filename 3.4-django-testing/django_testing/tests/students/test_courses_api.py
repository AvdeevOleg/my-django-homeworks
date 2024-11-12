import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == course.id

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    target_course = courses[0]
    url = reverse('courses-list')
    response = api_client.get(url, {'id': target_course.id})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == target_course.id

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course_factory(name='Math')
    course_factory(name='Science')
    url = reverse('courses-list')
    response = api_client.get(url, {'name': 'Math'})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Math'

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('courses-list')
    data = {'name': 'History'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'History'

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    data = {'name': 'Updated Course'}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Updated Course'

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
