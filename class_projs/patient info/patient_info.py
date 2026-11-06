class patient():
    def __init__(self,firstname,lastname,address,number,charges) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.number = number
        self.charges = charges
        self._doctor_discount = 0
        self._hospital_discount = 0
        self._payment_discount = 0
        self._government_discount = 5

    @property
    def doctor_discount(self):
        return self._doctor_discount

    @doctor_discount.setter
    def doctor_discount(self,num):
        if 0 <= num <= 5:
            self._doctor_discount = num
        else:
            print("invalid amount for Doctor Discount")

    @property
    def hospital_discount(self):
        return self._hospital_discount

    @hospital_discount.setter
    def hospital_discount(self,num):
        if 0 <= num <= 10:
            self._hospital_discount = num
        else:
            print("invalid amount for Hospital Discount")

    @property
    def payment_discount(self):
        return self._payment_discount

    @payment_discount.setter
    def payment_discount(self,num):
        if 0 <= num <= 15:
            self._payment_discount = num
        else:
            print("invalid amount for Payment Discount")

    @property
    def government_discount(self):
        return self._government_discount

    def __str__(self) -> str:
        return f"""patient full name: {self.firstname,self.lastname}
                    address: {self.address}
                    phone number: {self.charges}
                    total charges: {self.charges}"""

    def final_charges(self,charges):
        d = self.doctor_discount + self.payment_discount + self.government_discount + self.hospital_discount
        charges = self.charges - ((d/100) * charges)
        return charges
def main():
    p1 = patient("amir","amiri","tehran,pahlavi st.","123456",100000)


    p1.doctor_discount = 77
    p1.hospital_discount = 24
    p1.payment_discount = 5

    print("payment info".center(50,'-'))
    print(f"Doctor discount: {p1.doctor_discount}")
    print(f"Hospital discount: {p1.hospital_discount}")
    print(f"one-time payment discount: {p1.payment_discount}")
    print(f"Government discount: {p1.government_discount}")
    print(f"final charges: {p1.final_charges(p1.charges)}")

if __name__ == "__main__":
    main()
