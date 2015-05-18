#include <stdio.h>
#include <Windows.h>
#include "tmctl.h"

/* Get following input from server
1. IP Address
	1. Interface (USB/Ethernet)
2. Log duration
3. Output csv file
4. Data update interval
5. Parameters (voltage, current, power, energy)
6. Mode (RMS, DC)*/

/* Output csv file format
<Timestamp><Voltage><Current><Accumulated Energy><Avg Power>*/



int ExecuteCommunicate(void);


void main()
{
	printf("Hello World\n");
	ExecuteCommunicate();
}


int ExecuteCommunicate(void)
{
	char adr[100];
	int  ret;
	int  id;
	char buf[1000];
	int  length;

	ret = TmcInitialize(TM_CTL_VXI11, "192.168.1.3", &id);

	ret = TmcSetTerm(id, 2, 1);
	if (ret != 0) {
		return	TmcGetLastError(id);
	}
	ret = TmcSetTimeout(id, 300);
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	ret = TmcSetRen(id, 1);
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	/* sending *RST */
	ret = TmcSend(id, "*RST");
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	/* *sending IDN? & receiving query */
	ret = TmcSend(id, "*IDN?");
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	ret = TmcReceive(id, buf, 1000, &length);
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	/* *sending commands & receiving query */
	ret = TmcSend(id, ":INPUT:MODE DC");
	if (ret != 0) {
		return	TmcGetLastError(id);
	}


	/* *sending commands & receiving query */
	ret = TmcSend(id, ":NUMERIC:NORMAL:ITEM1 U,1");
	if (ret != 0) {
		return	TmcGetLastError(id);
	}

	/* *sending commands & receiving query */
	ret = TmcSend(id, ":NUMERIC:NORMAL:VALUE?");
	if (ret != 0) {
		return	TmcGetLastError(id);
	}
	ret = TmcReceive(id, buf, 1000, &length);
	if (ret != 0) {
		return	TmcGetLastError(id);
	}


}