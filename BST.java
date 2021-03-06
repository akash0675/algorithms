public class BinarySearchTree
{
public BinarySearchTree( )
{
        root = null;
    }
    
    public void insert( Comparable x )
    {
        root = insert( x, root );
    }
    
    public void remove( Comparable x )
    {
        root = remove( x, root );
    }
    
    public Comparable findMin( )
    {
        return elementAt( findMin( root ) );
    }
    
    public Comparable findMax( )
    {
        return elementAt( findMax( root ) );
    }
    
    public Comparable find( Comparable x )
    {
        return elementAt( find( x, root ) );
    }
    
    public void makeEmpty( )
    {
        root = null;
    }
    
    public boolean isEmpty( )
    {
        return root == null;
    }
    
    public void printTree( )
    {
        if( isEmpty( ) )
            System.out.println( "Empty tree" );
        else
            printTree( root );
    }
    
    private Comparable elementAt( BinaryNode t )
    {
        return t == null ? null : t.element;
    }
    
    private BinaryNode insert( Comparable x, BinaryNode t )
    {
        if( t == null )
            t = new BinaryNode( x, null, null );
        else if( x.compareTo( t.element ) < 0 )
            t.left = insert( x, t.left );
        else if( x.compareTo( t.element ) > 0 )
            t.right = insert( x, t.right );
        else
            ;
        return t;
    }
    
    private BinaryNode remove( Comparable x, BinaryNode t )
    {
        if( t == null )
            return t;
        if( x.compareTo( t.element ) < 0 )
            t.left = remove( x, t.left );
        else if( x.compareTo( t.element ) > 0 )
            t.right = remove( x, t.right );
        else if( t.left != null && t.right != null )
        {
            t.element = findMin( t.right ).element;
            t.right = remove( t.element, t.right );
        }
        else
            t = ( t.left != null ) ? t.left : t.right;
        return t;
    }
    
    private BinaryNode findMin( BinaryNode t )
    {
        if( t == null )
            return null;
        else if( t.left == null )
            return t;
        return findMin( t.left );
    }
    
    private BinaryNode findMax( BinaryNode t )
    {
        if( t != null )
            while( t.right != null )
                t = t.right;
        return t;
    }
    
    private BinaryNode find( Comparable x, BinaryNode t )
    {
        if( t == null )
            return null;
        if( x.compareTo( t.element ) < 0 )
            return find( x, t.left );
        else if( x.compareTo( t.element ) > 0 )
            return find( x, t.right );
        else
            return t;
    }
    
    private void printTree( BinaryNode t )
    {
        if( t != null )
        {
            printTree( t.left );
            System.out.println( t.element );
            printTree( t.right );
        }
    }
    
    private BinaryNode root;
    
    public static void main( String [ ] args )
    {
        BinarySearchTree t = new BinarySearchTree( );
        final int NUMS = 4000;
        final int GAP  =   37;
        System.out.println( "Checking... (no more output means success)" );
        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            t.insert( new MyInteger( i ) );
        for( int i = 1; i < NUMS; i+= 2 )
            t.remove( new MyInteger( i ) );
        if( NUMS < 40 )
            t.printTree( );
        if( ((MyInteger)(t.findMin( ))).intValue( ) != 2 ||
            ((MyInteger)(t.findMax( ))).intValue( ) != NUMS - 2 )
            System.out.println( "FindMin or FindMax error!" );
        for( int i = 2; i < NUMS; i+=2 )
             if( ((MyInteger)(t.find( new MyInteger( i ) ))).intValue( ) != i )
                 System.out.println( "Find error1!" );
        for( int i = 1; i < NUMS; i+=2 )
        {
            if( t.find( new MyInteger( i ) ) != null )
                System.out.println( "Find error2!" );
        }
    }
}