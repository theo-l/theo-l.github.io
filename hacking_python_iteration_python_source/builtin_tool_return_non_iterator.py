from base_demo import Iterable

if __name__ == "__main__":
    iterable_object = Iterable([1,2,3,4,6,5])

    sorted_result = sorted(iterable_object)
    print('\n', '<SORTED> function iteration context:', sorted_result, type(sorted_result), f'\n{"-"*50}\n' )

    sum_result = sum(iterable_object)
    print('\n', '<SUM> function iteration context:', sum_result, type(sum_result), f'\n{"-"*50}\n' )

    max_result = max(iterable_object)
    print('\n', '<MAX> function iteration context:', max_result, type(max_result), f'\n{"-"*50}\n' )

    min_result = min(iterable_object)
    print('\n', '<MIN> function iteration context:', min_result, type(min_result), f'\n{"-"*50}\n' )


    all_result = all(iterable_object)
    print('\n', '<ALL> function iteration context:', all_result, type(all_result), f'\n{"-"*50}\n' )

    any_result = any(iterable_object)
    print('\n', '<ANY> function iteration context:', any_result, type(any_result), f'\n{"-"*50}\n' )

