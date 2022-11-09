static decrypt (from, size,key){
	auto i,x;
	for (i=0;i<size;i=i+1){
		x=Byte(from);
		x=(x^key);
		PatchByte(from,x);
		from=from+1;
		}
	}
