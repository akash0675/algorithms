//Double LinkedList

class listNode{
	private int data;
	private listNode next;
	private listNode prev;

	public listNode(int data){
		this.data = data;
		this.prev = null;
		this.next = null;
	}

	public listNode(int data, listNode prev, listNode next){
		this.data = data;
		this.next = next;
		this.prev = prev;
	}

	public int getData(){
		return data;
	}

	public void setData(int data){
		this.data = data;
	}

	public void setPrev(listNode prev){
		this.prev = prev;
	}

	public listNode getPrev(){
		return this.prev;
	}

	public void setNext(listNode next){
		this.next = next;
	}

	public listNode getNext(){
		return this.next;
	}
}

class DoublyLinkedList{
	listNode head;
	listNode tail;
	private int length = 0;

	public DoublyLinkedList(){
		head = new listNode(Integer.MIN_VALUE, null, tail);
		head.setNext(tail);
		tail = new listNode(Integer.MIN_VALUE, head, null);
		tail.setPrev(head);
		length = 0;
	}

	public void insertAtBeginning(int data){
		listNode newNode = new listNode(data);
		listNode current = head.getNext();
		head.setNext(newNode);
		tail.setPrev(newNode);
		newNode.setPrev(head);
		newNode.setNext(current);
		length++;
	}

	public void print(){
		listNode current = head.getNext();
		while(current != null){
			System.out.println(current.getData());
			current = current.getNext();
		}
	}
}

class DLL{
	public static void main(String args[]){
		DoublyLinkedList a = new DoublyLinkedList();
		a.insertAtBeginning(10);
		a.insertAtBeginning(20);
		a.insertAtBeginning(30);
		a.insertAtBeginning(40);
		a.insertAtBeginning(50);
		a.print();
	}
}
