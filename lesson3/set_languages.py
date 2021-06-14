students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
lang_for_everyone, lang_for_someone = set.intersection(*students), set.union(*students)
print(len(lang_for_everyone), *sorted(lang_for_everyone), sep='\n')
print(len(lang_for_someone), *sorted(lang_for_someone), sep='\n')
