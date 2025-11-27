import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest 
{

    @Test
    public void testAddition() 
    {
        assertEquals(4, Calculator.add(2, 2));
    }

    @Test
    public void testSubtraction() 
    {
        assertEquals(2, Calculator.subtract(5, 3));
    }
}
