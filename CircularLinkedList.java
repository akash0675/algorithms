class CLLNode{
	private int data;
	private CLLNode next;

	public CLLNode(int data){this.data = data;}
	public void setData(int data){this.data = data;}
	public int getData(){return this.data;}
	public void setNext(CLLNode next){this.next = next;}
	public CLLNode getNext(){return this.next;}
}

class CLL{
	protected CLLNode tail;
	protected int length;
	
	public CLL(){
		tail = null;
		length = 0;
	}

	public void addToHead(int data){
		CLLNode temp = new CLLNode(data);
		if(tail == null){
			tail = temp;
			tail.setNext(tail);
		}
		else{
			temp.setNext(tail.getNext());
			tail.setNext(temp);
		}
		length++;
	}

	public void print(){
		CLLNode current = tail.getNext();
		int count = 0;
		while(count != length){
			System.out.println(current.getData());
			current = current.getNext();
			count++;
		}
	}
}

class CircularLinkedList{
	public static void main(String args[]){
		CLL a = new CLL();
		a.addToHead(10);
		a.addToHead(20);
		a.addToHead(30);
		a.addToHead(40);
		a.addToHead(50);
		a.addToHead(60);
		a.addToHead(70);
		a.addToHead(80);
		a.print();
	}
}