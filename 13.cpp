#include <cassert>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <random>
#include <algorithm>
#include <iostream>

using std::swap;
using std::vector;
using std::cout;
using std::cin;
using std::endl;

using TYPE = long;
static const size_t SORT_THRESHOLD = 16;

long* hoare_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *pivot_pos;
    for (;;) {
        ++first;
        auto f = *first;
        while (f < pivot)
            f = *++first;
        auto l = *last;
        while (pivot < l)
            l = *--last;
        if (first >= last)
            break;
        *first = l;
        *last = f;
        --last;
    }
    --first;
    swap(*first, *pivot_pos);
    return first;
}

long* lomuto_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;
    do {
        ++first;
    } while (*first < pivot);
    assert(first <= last);
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        if (x < pivot) {
            *read = *first;
            *first = x;
            ++first;
        }
    }
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}

long* lomuto_partition_branchfree(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first; // nothing interesting to do
    // Choose pivot.
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;
    // Prelude.
    do {
        ++first;
        assert(first <= last);
    } while (*first < pivot);
    // Main loop.
    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        auto less = -int(x < pivot);
        auto delta = less & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= less;
    }
    // Move the pivot to its final slot.
    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}

template<typename It>
void unguarded_linear_insert(It last) {
    auto val = *last;
    --last;
    auto x = *last;
    if (val >= x)
        return;
    for (;;) {
        last[1] = x;
        --last;
        x = *last;
        if (val >= x)
            break;
    }
    last[1] = val;
}

template<typename It>
void insertion_sort(It first, It last) {
    assert(first <= last);
    for (auto i = first + 1; i < last; ++i) {
        auto val = *i;
        if (val < *first) {
            size_t n = i - first - 1;
            do {
                first[n + 1] = first[n];
            } while (n--);
            *first = val;
        } else
            unguarded_linear_insert(i);
    }
}

template <class It>
void sort(It first, It last) {
    while (last - first > size_t(SORT_THRESHOLD)) {
        auto cut = hoare_partition(first, last);
        assert(cut >= first);
        assert(cut < last);
        sort(cut + 1, last);
        last = cut;
    }
    insertion_sort(first, last);
}

int main(int argc, char** argv) {
    size_t length;
    if (argc < 2) {
        cout << "Enter the length of the array: ";
        cin >> length;
    } else {
        length = atol(argv[1]);
    }

    if (length == 0) return 2;
    const size_t repeats = 50000000 / length;
    std::vector<double> times_hoare(repeats);
    std::vector<double> times_lomuto(repeats);
    std::vector<double> times_lomuto_branchfree(repeats);
    timespec start, end;

    std::mt19937 g(1942);
    std::vector<TYPE> v(length);
    vector<int> nums(length);

    // Lomuto's partition branch-free time
    for (size_t i = 0; i < repeats; ++i) {
        std::shuffle(v.begin(), v.end(), g);
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start);
        lomuto_partition_branchfree(&v.front(), 1 + &v.back());
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
        auto t = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
        times_lomuto_branchfree[i] = t;
    }
    std::sort(times_lomuto_branchfree.begin(), times_lomuto_branchfree.end());
    printf("Time taken by algorithm using Lomuto's partition with branch-free implementation (milliseconds): %.10lf\n", times_lomuto_branchfree[repeats / 2]);

    // Hoare's partition time
    for (size_t i = 0; i < repeats; ++i) {
        std::shuffle(v.begin(), v.end(), g);
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start);
        hoare_partition(&v.front(), 1 + &v.back());
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
        auto t = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
        times_hoare[i] = t;
    }
    std::sort(times_hoare.begin(), times_hoare.end());
    printf("Time taken by algorithm using Hoare's partition (milliseconds): %.10lf\n", times_hoare[repeats / 2]);

    // Lomuto's partition time
    for (size_t i = 0; i < repeats; ++i) {
        std::shuffle(v.begin(), v.end(), g);
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start);
        lomuto_partition(&v.front(), 1 + &v.back());
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
        auto t = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
        times_lomuto[i] = t;
    }
    std::sort(times_lomuto.begin(), times_lomuto.end());
    printf("Time taken by algorithm using Lomuto's partition (milliseconds): %.10lf\n", times_lomuto[repeats / 2]);
    
    /* 
       При различных входных данных от самого небольшого размера и по возрастанию
       отношение времени выполнения трех алгоритмов не меняется:
       алгоритм Хоара, как и положено, работает быстрее обычного алгоритма Ломуто,
       но алгорит Ломуто без ветвлений, неожиданно, работает медленне всех.

       Enter the length of the array: 100
       Time taken by algorithm using Lomuto's partition with branch-free implementation (milliseconds): 0.0017490000
       Time taken by algorithm using Hoare's partition (milliseconds): 0.0012560000
       Time taken by algorithm using Lomuto's partition (milliseconds): 0.0013400000
    */
    return 0;
}