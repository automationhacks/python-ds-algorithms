import heapq
import random


def test_given_a_list_then_list_can_be_converted_to_heap():
    numbers = [random.randint(1, 10) for i in range(10)]
    original_nums = numbers.copy()

    # heapify modifies the list in place
    # but does not sort, every sorted list satisfies
    # heap property
    heapq.heapify(numbers)
    assert numbers[0] == min(original_nums)

    print()
    print(f'Before: {original_nums}')
    print(f'After: {numbers}')


def test_given_a_heap_when_element_is_popped_then_smallest_element_is_popped():
    numbers = [random.randint(1, 10) for i in range(10)]
    heapq.heapify(numbers)

    smallest_number = min(numbers)
    popped_number = heapq.heappop(numbers)

    assert popped_number == smallest_number

def test_given_a_heap_when_element_is_pushed_then_heap_property_is_respected():
    numbers = [random.randint(3, 10) for i in range(10)]
    heapq.heapify(numbers)

    heapq.heappush(numbers, 2)
    assert numbers[0] == 2

def test_given_a_heap_then_n_smallest_numbers_could_be_found():
    numbers = [random.randint(3, 10) for i in range(10)]

    sorted_numbers = sorted(numbers)
    assert sorted_numbers[:3] == heapq.nsmallest(3, numbers)

def test_given_a_heap_then_n_largest_numbers_could_be_found():
    numbers = [random.randint(3, 10) for i in range(10)]

    sorted_numbers = sorted(numbers, reverse=True)
    assert sorted_numbers[:3] == heapq.nlargest(3, numbers)
