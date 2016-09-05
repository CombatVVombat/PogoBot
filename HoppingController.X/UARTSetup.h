/* 
 * File:   UARTSetup.h
 * Author: JRK
 *
 * Created on April 23, 2013, 6:23 PM
 */

#ifndef UARTSETUP_H
#define	UARTSETUP_H

#include <xc.h>
#include <stdint.h>
#include "stdio.h"

#define bufferSize 64

typedef struct SerialBuffer
{
    unsigned char index;
    char buffer[bufferSize];
} SerialBuffer;

extern SerialBuffer UART1Buffer;

void UARTSetup();
void putch(unsigned char byte);
void receiveSerial(struct SerialBuffer *SB);
void clearBuffer(struct SerialBuffer *SB);
char compareLastChar(const struct SerialBuffer *const SB, const char* c);
void CobsEncode(const uint8_t *const inputBuffer, const uint8_t inputBufferSize, uint8_t *const outputBuffer, const uint8_t outputBufferSize);
uint8_t addToBuffer(uint8_t *const buffer, const uint8_t index, const void *const data, const size_t size);

#endif	/* UARTSETUP_H */

