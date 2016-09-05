#include "T1Interrupt.h"
#include "PortsSetup.h"

uint32_t time = 0;
uint8_t inputBuffer[INPUT_BUFFER_SIZE];
uint8_t outputBuffer[OUTPUT_BUFFER_SIZE];

void __attribute__((__interrupt__, no_auto_psv)) _T1Interrupt(void)
{
    IFS0bits.T1IF = 0;
    updateEncoderPosition();
    updateEncoderVelocitySimple();
    int8_t power = 0;

    if(encoder.velocity > 8)
        power = 100;
    if(encoder.velocity < -8)
        power = -100;
    SetPowerOpenLoop(power);
    
    // Set inputBuffer size in T1Interrupt.h to fit these values
    uint8_t i = 0;
    i = addToBuffer(inputBuffer, i, &time, 4);                              // 4 Bytes
    i = addToBuffer(inputBuffer, i, (uint32_t*)&encoder.position, 4);       // 4 Bytes
    i = addToBuffer(inputBuffer, i, (uint16_t*)&encoder.velocity, 2);       // 2 Bytes
    i = addToBuffer(inputBuffer, i, (uint8_t*)&power, 1);                   // 1 Bytes      // Totals 11 Bytes

    CobsEncode(inputBuffer, INPUT_BUFFER_SIZE, outputBuffer, OUTPUT_BUFFER_SIZE);

    for(int i = 0; i < OUTPUT_BUFFER_SIZE; ++i)
    {
        putch(outputBuffer[i]); 
    }
    putch(0);

    time++;
}
