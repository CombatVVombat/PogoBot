#include "UARTSetup.h"

SerialBuffer UART1Buffer;

void UARTSetup()
{
    U1MODEbits.BRGH = 1;
    U1BRG = 299;            // 57600
    U1MODEbits.PDSEL = 0;   // 8bits, No Parity
    U1MODEbits.STSEL = 0;   // 1 Stop bit
    U1MODEbits.URXINV = 1;  // Receive Polarity Invert
    U1MODEbits.ABAUD = 0;   // AutoBaud OFF
    U1MODEbits.LPBACK = 0;  // Loopback disabled
    U1MODEbits.WAKE = 0;    // Wake-up disabled

    U1STAbits.UTXINV = 1;   // Transmit Polarity Invert
    U1STAbits.ADDEN = 0;    // Address Mode disabled

    U1MODEbits.UARTEN = 1;  // Enable UART1
    U1STAbits.UTXEN = 1;    // Transmit Enabled
}

void putch(unsigned char byte)
{
    // Puts a byte onto the output serial register
    while(!U1STAbits.TRMT);
    U1TXREG = byte;
}

void clearBuffer(SerialBuffer *SB)
{
    for(int i = 0; i < bufferSize; i++)
    {
        SB->buffer[i] = 0;
    }
    SB->index = 0;
}

void receiveSerial(SerialBuffer *SB)
{
    if(U1STAbits.OERR)  // Check Overrun
        printf("Serial Buffer Overrun\n");
    if(U1STAbits.FERR)
        printf("Framing Error\n");
    if(U1STAbits.PERR)
        printf("Parity Error\n");
    if(U1STAbits.URXDA)
    {
        if(SB->index < (bufferSize-1))               // Check buffer is not full
        {
            SB->index++;
            SB->buffer[SB->index]= U1RXREG;         // Take character from RX line into buffer
            printf("%c", SB->buffer[SB->index]);    // Echo to console
        }
        else
        {
            clearBuffer(SB);
        }
    }
}

void CobsEncode(const uint8_t *const inputBuffer, const uint8_t inputBufferSize, uint8_t *const outputBuffer, const uint8_t outputBufferSize)
{
    uint8_t outputBufferIndex = 0;
    uint8_t bytesExamined = 0;

    for(uint8_t i = 0; i <= inputBufferSize; ++i)
    {
        uint8_t value = 0;
        if(i < inputBufferSize)
            value = inputBuffer[i];     // Value remains zero if past end of inputBuffer (implicit terminating zero)

        ++bytesExamined;
        if(value == 0) // Found a zero
        {
            outputBuffer[outputBufferIndex] = bytesExamined;    // Put Code value
            ++outputBufferIndex;
            uint8_t first = i-bytesExamined+1;
            uint8_t last = i;
            for(int q = first; q < last; ++q)
            {
                if(outputBufferIndex >= outputBufferSize)
                    break;
                outputBuffer[outputBufferIndex] = inputBuffer[q];
                ++outputBufferIndex;
            }
            bytesExamined = 0;
        }
    }
}

char compareLastChar(const SerialBuffer *const SB, const char* c)
{
    if(SB->buffer[SB->index] == *c)
        return 1;
    else
        return 0;
}

uint8_t addToBuffer(uint8_t *const buffer, const uint8_t index, const void *const data, const size_t size)
{
    // Add byte(s) to a buffer.
    // index = where to write the first byte
    // size = # bytes to write
    // returns next index
    uint8_t *ptr = (uint8_t *)data;     // cast to u_char pointer type for incrementing purposes
    for(uint8_t i = index; i < index+size; ++i)
    {
        buffer[i] = *ptr;
        ++ptr;
    }
    return index+size;
}




