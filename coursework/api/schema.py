import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Teacher, Student, Subject


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject


class Query(ObjectType):
    teacher = graphene.Field(TeacherType, id=graphene.Int())
    student = graphene.Field(StudentType, id=graphene.Int())
    subject = graphene.Field(SubjectType, id=graphene.Int())
    teachers = graphene.List(TeacherType)
    students = graphene.List(StudentType)
    subjects = graphene.List(SubjectType)

    def resolve_teacher(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Teacher.objects.get(pk=id)
        return None

    def resolve_student(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Student.objects.get(pk=id)
        return None

    def resolve_subject(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Subject.objects.get(pk=id)
        return None

    def resolve_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_subjects(self, info, **kwargs):
        return Subject.objects.all()


class TeacherInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()


class StudentInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    rollno = graphene.Int()
    mentor = graphene.List(TeacherInput)


class SubjectInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    subcode = graphene.String()
    teachers = graphene.List(TeacherInput)
    students = graphene.List(StudentInput)


class CreateTeacher(graphene.Mutation):
    class Arguments:
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        teacher_instance = Teacher(name=input.name, email=input.email)
        teacher_instance.save()
        return CreateTeacher(ok=ok, teacher=teacher_instance)


class UpdateTeacher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        teacher_instance = Teacher.objects.get(pk=id)
        if teacher_instance:
            ok = True
            teacher_instance.name = input.name
            teacher_instance.email = input.email
            teacher_instance.save()
            return UpdateTeacher(ok=ok, teacher=teacher_instance)
        return UpdateTeacher(ok=ok, teacher=None)


class CreateStudent(graphene.Mutation):
    class Arguments:
        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        mentor = []
        for teacher_input in input.mentor:
            teacher = Teacher.objects.get(pk=teacher_input.id)
            if teacher is None:
                return CreateStudent(ok=False, movie=None)
            mentor.append(teacher)
        student_instance = Student(
            name=input.name, email=input.email, rollno=input.rollno
        )
        student_instance.save()
        student_instance.mentor.set(mentor)
        return CreateStudent(ok=ok, student=student_instance)


class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        student_instance = Student.objects.get(pk=id)
        if student_instance:
            ok = True
            mentor = []
            for teacher_input in input.mentor:
                teacher = Teacher.objects.get(pk=teacher_input.id)
                if teacher is None:
                    return CreateStudent(ok=False, movie=None)
                mentor.append(teacher)
            student_instance.name = input.name
            student_instance.email = input.email
            student_instance.rollno = input.rollno
            student_instance.save()
            student_instance.mentor.set(mentor)
            return UpdateStudent(ok=ok, student=student_instance)
        return UpdateStudent(ok=ok, student=None)


class CreateSubject(graphene.Mutation):
    class Arguments:
        input = SubjectInput(required=True)

    ok = graphene.Boolean()
    subject = graphene.Field(SubjectType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        students = []
        for student_input in input.students:
            student = Student.objects.get(pk=student_input.id)
            if student is None:
                return CreateSubject(ok=False, movie=None)
            students.append(student)
        teachers = []
        for teacher_input in input.teachers:
            teacher = Teacher.objects.get(pk=teacher_input.id)
            if teacher is None:
                return CreateSubject(ok=False, movie=None)
            teachers.append(teacher)
        subject_instance = Subject(name=input.name, subcode=input.subcode)
        subject_instance.save()
        subject_instance.teachers.set(teachers)
        subject_instance.students.set(students)
        return CreateSubject(ok=ok, subject=subject_instance)


class UpdateSubject(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = SubjectInput(required=True)

    ok = graphene.Boolean()
    subject = graphene.Field(SubjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        subject_instance = Subject.objects.get(pk=id)
        if subject_instance:
            ok = True
            teachers = []
            for teacher_input in input.teachers:
                teacher = Teacher.objects.get(pk=teacher_input.id)
                if teacher is None:
                    return CreateSubject(ok=False, movie=None)
                teachers.append(teacher)
            students = []
            for student_input in input.students:
                student = Student.objects.get(pk=student_input.id)
                if student is None:
                    return CreateSubject(ok=False, movie=None)
                students.append(student)
            subject_instance.name = input.name
            subject_instance.subcode = input.subcode
            subject_instance.save()
            subject_instance.teachers.set(teachers)
            subject_instance.students.set(students)
            return UpdateSubject(ok=ok, subject=subject_instance)
        return UpdateSubject(ok=ok, subject=None)


class Mutation(graphene.ObjectType):
    create_teacher = CreateTeacher.Field()
    update_teacher = UpdateTeacher.Field()
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    create_subject = CreateSubject.Field()
    update_subject = UpdateSubject.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
