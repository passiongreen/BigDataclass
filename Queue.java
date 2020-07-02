package JC;

import java.util.LinkedList;

public class Queue {
    
    public static void main(String[] args) {
        LinkedList<String> is = new LinkedList<String>();

        is.offer("홍길동");
        is.offer("김동자");
        is.offer("유명한");
        is.offer("천세원");

        System.out.println("Size =" + is.size());

        while(is.peek() != null)
            System.out.println(is.poll());

        System.out.println("Size =" + is.size());
    }
}