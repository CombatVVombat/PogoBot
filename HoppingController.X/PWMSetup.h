/* 
 * File:   PWMSetup.h
 * Author: JRK
 *
 * Created on April 23, 2013, 6:26 PM
 */

#ifndef PWMSETUP_H
#define	PWMSETUP_H

#include <xc.h>
#include "PortsSetup.h"

#define PWM_PERIOD 8192

void EnablePWM();
void DisablePWM();
void PWMSetup();
void SetPowerOpenLoop(signed char Percent);

#endif	/* PWMSETUP_H */

