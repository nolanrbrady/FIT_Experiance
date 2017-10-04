public class Version:IEntity
    {
        public int Id { get; set; }
        public int QuestionId { get; set; }
        public int VersionNumber { get; set; }
        public int UserId { get; set; }
        public DateTime CreateDate { get; set; }
        public string QuestionContent { get; set; }
    }

