# p876-middle-of-the-linked-list
[https://leetcode.com/problems/middle-of-the-linked-listn/](https://leetcode.com/problems/middle-of-the-linked-listn/)

## Initial provided code
```Typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function middleNode(head: ListNode | null): ListNode | null {

};
```

## First approach - Iterative

In this case, I iterated throw the linked list and copy each node to an `array`. After this, a returned the `array[n / 2]` to get the middle node.

### Solution

- n = number of nodes
- time complexity: O(n)
- space complexity: O(n)

## Second approach - Pointers

Copying an array, makes the space complexity increases a lot. As you can observe, in the first approach, the space complexity is O(n).

So, I started thinking how could I find the middle node without another data structure (like the array that I used before).

So I started trying to find some pattern:
- [<u>**1**</u>] => 1
- [1, <u>2</u>] => 2
- [1, <u>2</u>, 3] => 2
- [1, 2, <u>3</u>, 4] => 3
- [1, 2, <u>3</u>, 4, 5] => 3  
- [1, 2, 3, <u>4</u>, 5, 6] => 4
- [1, 2, 3, <u>4</u>, 5, 6, 7] => 4

As you can notice, as the size of my list grows by 2, my middle node moves up. So every time that <u>my current end node</u> and <u>the next of the current end node</u> are not null: `mid = mid.next` and `end = end.next.next`.


- n = number of nodes
- time complexity: O(n)
- space complexity: O(1)

