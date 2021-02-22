from django.shortcuts import render

# Create your views here.

list_rounds = {}
rounds = 1




def game(actual):
    secret_nums = [5, 1, 2, 9]

    cow = 0
    bull = 0

    if len(actual) != 4:
        return 'Wrong numbers count (required 4 numbers) or incorrect input form. You have to type numbers using space (for example 1 2 3 4)'
    for i in range(len(secret_nums)):
        if secret_nums[i] == actual[i]:
            bull += 1
        elif actual[i] in secret_nums:
            cow += 1
        if bull == 4:
            return 'You win!'
    return f'Cows: {cow}; Bulls: {bull}'

def results(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        actual = list(map(int,request.POST.get('numbers').split(' ')))
        context = {'result': game(actual)}
        return render(request, 'index.html', context)

def history_page(request):
    return render(request, 'rounds.html')
