import math

a,b,c=map(int,input().split())

def a_rsqrtf(float a, const float _exc) :
    if (a > 0.0f) :
        const float t_2r2rt[] = {1.00000000000000000E+00f, 1.41421356237309505E+00f}
        long e
        float h, r = 1.82842712474619010E+00f - 8.28427124746190100E-01f * frexpf(a, &e)
        
        r  = ldexpf(r * t_2r2rt[e & 0x00000001], -e >> 1)
        h  = a * r * r
        r *= 1.875f - h * (1.25f - h * 0.375f)
        a *= 0.5f
        r *= 1.5f - a * r * r
        r *= 1.5f - a * r * r
        
        return r
    
    
    return _exc


if((math.sqrt(a)+math.sqrt(b))<math.sqrt(c)):
    print("Yes")
else:
    print("No")



